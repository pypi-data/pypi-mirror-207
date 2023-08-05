import mythic_container
from mythic_container.logging import logger

MYTHIC_RPC_PAYLOAD_SEARCH = "mythic_rpc_payload_search"

class MythicRPCPayloadSearchBuildParameter:
    def __init__(self,
                 PayloadType: str = None,
                 BuildParameterValues: dict = None,
                 **kwargs):
        self.PayloadType = PayloadType
        self.BuildParameterValues = BuildParameterValues
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "payload_type": self.PayloadType,
            "build_parameter_values": self.BuildParameterValues
        }

class MythicRPCPayloadSearchMessage:
    def __init__(self,
                 CallbackID: int = None,
                 PayloadUUID: str = None,
                 Description: str = None,
                 Filename: str = None,
                 PayloadTypes: list[str] = None,
                 IncludeAutoGeneratedPayloads: bool = None,
                 BuildParameters: list[MythicRPCPayloadSearchBuildParameter] = [],
                 **kwargs):
        self.CallbackID = CallbackID
        self.PayloadUUID = PayloadUUID
        self.Description = Description
        self.Filename = Filename
        self.PayloadTypes = PayloadTypes
        self.IncludeAutoGeneratedPayloads = IncludeAutoGeneratedPayloads
        self.BuildParameters = BuildParameters
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "callback_id": self.CallbackID,
            "uuid": self.PayloadUUID,
            "description": self.Description,
            "filename": self.Filename,
            "payload_types": self.PayloadTypes,
            "include_auto_generated": self.IncludeAutoGeneratedPayloads,
            "build_parameters": [x.to_json() for x in self.BuildParameters]
        }

class MythicRPCPayloadConfigurationC2Profile:
    def __init__(self,
                 c2_profile: str,
                 c2_profile_parameters: dict,
                 **kwargs):
        self.Name = c2_profile
        self.Parameters = c2_profile_parameters
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")
    def to_json(self):
        return {
            "c2_profile": self.Name,
            "c2_profile_parameters": self.Parameters
        }
class MythicRPCPayloadConfigurationBuildParameter:
    def __init__(self,
                 name: str,
                 value: any,
                 **kwargs):
        self.Name = name
        self.Value = value
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")
    def to_json(self):
        return {
            "name": self.Name,
            "value": self.Value
        }
class MythicRPCPayloadConfiguration:
    def __init__(self,
                 description: str = None,
                 payload_type: str = None,
                 c2_profiles: list[MythicRPCPayloadConfigurationC2Profile] = None,
                 build_parameters: list[MythicRPCPayloadConfigurationBuildParameter] = None,
                 commands: list[str] = None,
                 selected_os: str = None,
                 filename: str = None,
                 wrapped_payload: str = None,
                 uuid: str = None,
                 agent_file_id: str = None,
                 build_phase: str = None,
                 **kwargs):
        self.Description = description
        self.PayloadType = payload_type
        if c2_profiles is not None:
            if isinstance(c2_profiles, list):
                self.C2Profiles = [MythicRPCPayloadConfigurationC2Profile(**x) for x in c2_profiles]
            else:
                self.C2Profiles = c2_profiles
        else:
            self.C2Profiles = None
        if build_parameters is not None:
            if isinstance(build_parameters, list):
                self.BuildParameters = [MythicRPCPayloadConfigurationBuildParameter(**x) for x in build_parameters]
            else:
                self.BuildParameters = build_parameters
        else:
            self.BuildParameters = None
        self.Commands = commands
        self.SelectedOS = selected_os
        self.Filename = filename
        self.WrappedPayloadUUID = wrapped_payload
        self.UUID = uuid
        self.AgentFileId = agent_file_id
        self.BuildPhase = build_phase
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "description": self.Description,
            "payload_type": self.PayloadType,
            "c2_profiles": [x.to_json() for x in self.C2Profiles],
            "build_parameters": [x.to_json() for x in self.BuildParameters],
            "commands": self.Commands,
            "selected_os": self.SelectedOS,
            "filename": self.Filename,
            "wrapped_payload": self.WrappedPayloadUUID,
            "uuid": self.UUID,
            "agent_file_id": self.AgentFileId,
            "build_phase": self.BuildPhase
        }
class MythicRPCPayloadSearchMessageResponse:
    Payloads: list[MythicRPCPayloadConfiguration]

    def __init__(self,
                 success: bool = False,
                 error: str = "",
                 payloads: list[dict] = None,
                 **kwargs):
        self.Success = success
        self.Error = error
        self.Payloads = [MythicRPCPayloadConfiguration(**x) for x in payloads] if payloads is not None else []
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")


async def SendMythicRPCPayloadSearch(
        msg: MythicRPCPayloadSearchMessage) -> MythicRPCPayloadSearchMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_PAYLOAD_SEARCH,
                                                                            body=msg.to_json())
    return MythicRPCPayloadSearchMessageResponse(**response)
