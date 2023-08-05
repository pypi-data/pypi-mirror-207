import importlib
import logging
from contextlib import suppress
from typing import Optional, Dict, Any
from typing import TYPE_CHECKING

from pyhon import helper
from pyhon.commands import HonCommand
from pyhon.parameter.base import HonParameter
from pyhon.parameter.fixed import HonParameterFixed

if TYPE_CHECKING:
    from pyhon import HonAPI

_LOGGER = logging.getLogger(__name__)


class HonAppliance:
    def __init__(
        self, api: Optional["HonAPI"], info: Dict[str, Any], zone: int = 0
    ) -> None:
        if attributes := info.get("attributes"):
            info["attributes"] = {v["parName"]: v["parValue"] for v in attributes}
        self._info: Dict = info
        self._api: Optional[HonAPI] = api
        self._appliance_model: Dict = {}

        self._commands: Dict = {}
        self._statistics: Dict = {}
        self._attributes: Dict = {}
        self._zone: int = zone
        self._additional_data = {}

        try:
            self._extra = importlib.import_module(
                f"pyhon.appliances.{self.appliance_type.lower()}"
            ).Appliance(self)
        except ModuleNotFoundError:
            self._extra = None

    def __getitem__(self, item):
        if self._zone:
            item += f"Z{self._zone}"
        if "." in item:
            result = self.data
            for key in item.split("."):
                if all(k in "0123456789" for k in key) and isinstance(result, list):
                    result = result[int(key)]
                else:
                    result = result[key]
            return result
        if item in self.data:
            return self.data[item]
        if item in self.attributes["parameters"]:
            return self.attributes["parameters"].get(item)
        return self.info[item]

    def get(self, item, default=None):
        try:
            return self[item]
        except (KeyError, IndexError):
            return default

    def _check_name_zone(self, name: str, frontend: bool = True) -> str:
        middle = " Z" if frontend else "_z"
        if (attribute := self._info.get(name, "")) and self._zone:
            return f"{attribute}{middle}{self._zone}"
        return attribute

    @property
    def appliance_model_id(self) -> str:
        return self._info.get("applianceModelId", "")

    @property
    def appliance_type(self) -> str:
        return self._info.get("applianceTypeName", "")

    @property
    def mac_address(self) -> str:
        return self.info.get("macAddress", "")

    @property
    def unique_id(self) -> str:
        return self._check_name_zone("macAddress", frontend=False)

    @property
    def model_name(self) -> str:
        return self._check_name_zone("modelName")

    @property
    def nick_name(self) -> str:
        return self._check_name_zone("nickName")

    @property
    def commands_options(self):
        return self._appliance_model.get("options")

    @property
    def commands(self):
        return self._commands

    @property
    def attributes(self):
        return self._attributes

    @property
    def statistics(self):
        return self._statistics

    @property
    def info(self):
        return self._info

    @property
    def additional_data(self):
        return self._additional_data

    @property
    def zone(self) -> int:
        return self._zone

    async def _recover_last_command_states(self):
        command_history = await self._api.command_history(self)
        for name, command in self._commands.items():
            last = next(
                (
                    index
                    for (index, d) in enumerate(command_history)
                    if d.get("command", {}).get("commandName") == name
                ),
                None,
            )
            if last is None:
                continue
            parameters = command_history[last].get("command", {}).get("parameters", {})
            if command.categories and parameters.get("category"):
                command.category = parameters.pop("category").split(".")[-1].lower()
                command = self.commands[name]
            for key, data in command.settings.items():
                if (
                    not isinstance(data, HonParameterFixed)
                    and parameters.get(key) is not None
                ):
                    with suppress(ValueError):
                        data.value = parameters.get(key)

    def _get_categories(self, command, data):
        categories = {}
        for category, value in data.items():
            result = self._get_command(value, command, category, categories)
            if result:
                if "PROGRAM" in category:
                    category = category.split(".")[-1].lower()
                categories[category] = result[0]
        if categories:
            return [list(categories.values())[0]]
        return []

    def _get_commands(self, data):
        commands = []
        for command, value in data.items():
            commands += self._get_command(value, command, "")
        return {c.name: c for c in commands}

    def _get_command(self, data, command="", category="", categories=None):
        commands = []
        if isinstance(data, dict):
            if data.get("description") and data.get("protocolType", None):
                commands += [
                    HonCommand(
                        command,
                        data,
                        self._api,
                        self,
                        category_name=category,
                        categories=categories,
                    )
                ]
            else:
                commands += self._get_categories(command, data)
        else:
            self._additional_data[command] = data
        return commands

    async def load_commands(self):
        raw = await self._api.load_commands(self)
        self._appliance_model = raw.pop("applianceModel")
        raw.pop("dictionaryId")
        self._commands = self._get_commands(raw)
        await self._recover_last_command_states()

    async def load_attributes(self):
        self._attributes = await self._api.load_attributes(self)
        for name, values in self._attributes.pop("shadow").get("parameters").items():
            self._attributes.setdefault("parameters", {})[name] = values["parNewVal"]

    async def load_statistics(self):
        self._statistics = await self._api.load_statistics(self)

    async def update(self):
        await self.load_attributes()

    @property
    def parameters(self):
        result = {}
        for name, command in self._commands.items():
            for key, parameter in command.parameters.items():
                result.setdefault(name, {})[key] = parameter.value
        return result

    @property
    def settings(self):
        result = {}
        for name, command in self._commands.items():
            for key in command.setting_keys:
                setting = command.settings.get(key, HonParameter(key, {}, name))
                result[f"{name}.{key}"] = setting
        if self._extra:
            return self._extra.settings(result)
        return result

    @property
    def data(self):
        result = {
            "attributes": self.attributes,
            "appliance": self.info,
            "statistics": self.statistics,
            "additional_data": self._additional_data,
            **self.parameters,
        }
        if self._extra:
            return self._extra.data(result)
        return result

    @property
    def diagnose(self):
        data = self.data.copy()
        for sensible in ["PK", "SK", "serialNumber", "code", "coords"]:
            data["appliance"].pop(sensible, None)
        result = helper.pretty_print({"data": self.data}, whitespace="\u200B \u200B ")
        result += helper.pretty_print(
            {"commands": helper.create_command(self.commands)},
            whitespace="\u200B \u200B ",
        )
        return result.replace(self.mac_address, "xx-xx-xx-xx-xx-xx")
