""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class RedirectRecordsSchema(schema.ResponseSchema):
    """RedirectRecords - 访问明细"""

    fields = {
        "AccountID": fields.Int(required=True, load_from="AccountID"),
        "Browser": fields.Str(required=True, load_from="Browser"),
        "ClientIP": fields.Str(required=True, load_from="ClientIP"),
        "Os": fields.Str(required=True, load_from="Os"),
        "ProvinceCode": fields.Str(required=True, load_from="ProvinceCode"),
        "RedirectTime": fields.Int(required=True, load_from="RedirectTime"),
        "RequestTime": fields.Int(required=True, load_from="RequestTime"),
        "Scenario": fields.Str(required=True, load_from="Scenario"),
        "ScenarioID": fields.Int(required=True, load_from="ScenarioID"),
        "ShortLink": fields.Str(required=True, load_from="ShortLink"),
        "ShortLinkDomain": fields.Str(
            required=True, load_from="ShortLinkDomain"
        ),
    }


class SecondaryLinkForQuerySchema(schema.ResponseSchema):
    """SecondaryLinkForQuery - SecondaryLink查询实体"""

    fields = {
        "IsSecondary": fields.Bool(required=True, load_from="IsSecondary"),
        "LongLink": fields.Str(required=True, load_from="LongLink"),
        "LongLinkID": fields.Int(required=True, load_from="LongLinkID"),
        "Oses": fields.Str(required=True, load_from="Oses"),
        "ProvinceCodes": fields.Str(required=True, load_from="ProvinceCodes"),
        "Scenario": fields.Str(required=True, load_from="Scenario"),
        "ScenarioID": fields.Int(required=True, load_from="ScenarioID"),
        "ShortLongMapID": fields.Int(required=True, load_from="ShortLongMapID"),
    }


class ShortLinkSchema(schema.ResponseSchema):
    """ShortLink - 短链接返回模型"""

    fields = {
        "ClickCount": fields.Int(required=True, load_from="ClickCount"),
        "ClickCountToday": fields.Int(
            required=True, load_from="ClickCountToday"
        ),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DeleteTime": fields.Int(required=True, load_from="DeleteTime"),
        "EndTime": fields.Int(required=True, load_from="EndTime"),
        "ID": fields.Int(required=True, load_from="ID"),
        "LongLinks": fields.List(fields.Str()),
        "Operator": fields.Str(required=True, load_from="Operator"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "Scenario": fields.Str(required=True, load_from="Scenario"),
        "ScenarioDesc": fields.Str(required=True, load_from="ScenarioDesc"),
        "ScenarioID": fields.Int(required=True, load_from="ScenarioID"),
        "SecondaryLinks": fields.List(SecondaryLinkForQuerySchema()),
        "ShortLink": fields.Str(required=True, load_from="ShortLink"),
        "ShortLinkDomain": fields.Str(
            required=True, load_from="ShortLinkDomain"
        ),
        "StartTime": fields.Int(required=True, load_from="StartTime"),
        "Status": fields.Int(required=True, load_from="Status"),
        "Type": fields.Int(required=True, load_from="Type"),
        "UniqueClickCount": fields.Int(
            required=True, load_from="UniqueClickCount"
        ),
        "UniqueClickCountToday": fields.Int(
            required=True, load_from="UniqueClickCountToday"
        ),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
    }
