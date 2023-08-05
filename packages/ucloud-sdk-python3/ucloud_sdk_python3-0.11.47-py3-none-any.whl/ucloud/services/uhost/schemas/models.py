""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class KeyPairSchema(schema.ResponseSchema):
    """KeyPair - 密钥对信息"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "KeyPairFingerPrint": fields.Str(
            required=False, load_from="KeyPairFingerPrint"
        ),
        "KeyPairId": fields.Str(required=False, load_from="KeyPairId"),
        "KeyPairName": fields.Str(required=False, load_from="KeyPairName"),
        "PrivateKeyBody": fields.Str(
            required=False, load_from="PrivateKeyBody"
        ),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
    }


class CollectionSchema(schema.ResponseSchema):
    """Collection - CPU和内存可支持的规格"""

    fields = {
        "Cpu": fields.Int(required=False, load_from="Cpu"),
        "Memory": fields.List(fields.Int()),
        "MinimalCpuPlatform": fields.List(fields.Str()),
    }


class FeatureModesSchema(schema.ResponseSchema):
    """FeatureModes - 可以支持的模式类别"""

    fields = {
        "MinimalCpuPlatform": fields.List(fields.Str()),
        "Name": fields.Str(required=False, load_from="Name"),
        "RelatedToImageFeature": fields.List(fields.Str()),
    }


class DataDiskInfoSchema(schema.ResponseSchema):
    """DataDiskInfo - 数据盘信息"""

    fields = {
        "Features": fields.List(fields.Str()),
        "MaximalSize": fields.Int(required=False, load_from="MaximalSize"),
        "MinimalSize": fields.Int(required=False, load_from="MinimalSize"),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class BootDiskInfoSchema(schema.ResponseSchema):
    """BootDiskInfo - 系统盘信息"""

    fields = {
        "Features": fields.List(fields.Str()),
        "InstantResize": fields.Bool(required=False, load_from="InstantResize"),
        "MaximalSize": fields.Int(required=False, load_from="MaximalSize"),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class MachineSizesSchema(schema.ResponseSchema):
    """MachineSizes - GPU、CPU和内存信息"""

    fields = {
        "Collection": fields.List(CollectionSchema()),
        "Gpu": fields.Int(required=False, load_from="Gpu"),
    }


class GraphicsMemorySchema(schema.ResponseSchema):
    """GraphicsMemory - GPU的显存指标"""

    fields = {
        "Rate": fields.Int(required=False, load_from="Rate"),
        "Value": fields.Int(required=False, load_from="Value"),
    }


class FeaturesSchema(schema.ResponseSchema):
    """Features - 虚机可支持的特性"""

    fields = {
        "Modes": fields.List(FeatureModesSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class DisksSchema(schema.ResponseSchema):
    """Disks - 磁盘信息"""

    fields = {
        "BootDisk": fields.List(BootDiskInfoSchema()),
        "DataDisk": fields.List(DataDiskInfoSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class CpuPlatformsSchema(schema.ResponseSchema):
    """CpuPlatforms - CPU平台信息"""

    fields = {
        "Amd": fields.List(fields.Str()),
        "Ampere": fields.List(fields.Str()),
        "Intel": fields.List(fields.Str()),
    }


class PerformanceSchema(schema.ResponseSchema):
    """Performance - GPU的性能指标"""

    fields = {
        "Rate": fields.Int(required=False, load_from="Rate"),
        "Value": fields.Float(required=False, load_from="Value"),
    }


class AvailableInstanceTypesSchema(schema.ResponseSchema):
    """AvailableInstanceTypes - https://ushare.ucloudadmin.com/pages/viewpage.action?pageId=104662646"""

    fields = {
        "CpuPlatforms": CpuPlatformsSchema(),
        "Disks": fields.List(DisksSchema()),
        "Features": fields.List(FeaturesSchema()),
        "GraphicsMemory": GraphicsMemorySchema(),
        "MachineClass": fields.Str(required=False, load_from="MachineClass"),
        "MachineSizes": fields.List(MachineSizesSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "Performance": PerformanceSchema(),
        "Status": fields.Str(required=False, load_from="Status"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UHostImageSetSchema(schema.ResponseSchema):
    """UHostImageSet - DescribeImage"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Features": fields.List(fields.Str()),
        "FuncType": fields.Str(required=False, load_from="FuncType"),
        "ImageDescription": fields.Str(
            required=False, load_from="ImageDescription"
        ),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "Links": fields.Str(required=False, load_from="Links"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "State": fields.Str(required=False, load_from="State"),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class SpreadInfoSchema(schema.ResponseSchema):
    """SpreadInfo - 每个可用区中硬件隔离组信息"""

    fields = {
        "UHostCount": fields.Int(required=False, load_from="UHostCount"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class IsolationGroupSchema(schema.ResponseSchema):
    """IsolationGroup - 硬件隔离组信息"""

    fields = {
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SpreadInfoSet": fields.List(SpreadInfoSchema()),
    }


class UHostKeyPairSchema(schema.ResponseSchema):
    """UHostKeyPair - 主机密钥信息"""

    fields = {
        "KeyPairId": fields.Str(required=False, load_from="KeyPairId"),
        "KeyPairState": fields.Str(required=False, load_from="KeyPairState"),
    }


class UHostDiskSetSchema(schema.ResponseSchema):
    """UHostDiskSet - DescribeUHostInstance"""

    fields = {
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "Encrypted": fields.Str(required=False, load_from="Encrypted"),
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """UHostIPSet - DescribeUHostInstance"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
        "IP": fields.Str(required=False, load_from="IP"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IPMode": fields.Str(required=True, load_from="IPMode"),
        "Mac": fields.Str(required=False, load_from="Mac"),
        "NetworkInterfaceId": fields.Str(
            required=False, load_from="NetworkInterfaceId"
        ),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class UHostInstanceSetSchema(schema.ResponseSchema):
    """UHostInstanceSet - DescribeUHostInstance"""

    fields = {
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "BasicImageName": fields.Str(
            required=False, load_from="BasicImageName"
        ),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CloudInitFeature": fields.Bool(
            required=False, load_from="CloudInitFeature"
        ),
        "CpuPlatform": fields.Str(required=False, load_from="CpuPlatform"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "HostType": fields.Str(required=False, load_from="HostType"),
        "HotplugFeature": fields.Bool(
            required=False, load_from="HotplugFeature"
        ),
        "HpcFeature": fields.Bool(required=False, load_from="HpcFeature"),
        "IPSet": fields.List(UHostIPSetSchema()),
        "IPv6Feature": fields.Bool(required=False, load_from="IPv6Feature"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "IsolationGroup": fields.Str(
            required=False, load_from="IsolationGroup"
        ),
        "KeyPair": UHostKeyPairSchema(),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Name": fields.Str(required=False, load_from="Name"),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "RdmaClusterId": fields.Str(required=False, load_from="RdmaClusterId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RestrictMode": fields.Str(required=False, load_from="RestrictMode"),
        "State": fields.Str(required=False, load_from="State"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "TotalDiskSpace": fields.Int(
            required=False, load_from="TotalDiskSpace"
        ),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UHostSnapshotSetSchema(schema.ResponseSchema):
    """UHostSnapshotSet -"""

    fields = {
        "SnapshotName": fields.Str(required=False, load_from="SnapshotName"),
        "SnapshotState": fields.Str(required=False, load_from="SnapshotState"),
        "SnapshotTime": fields.Str(required=False, load_from="SnapshotTime"),
    }


class KeyPairDescSchema(schema.ResponseSchema):
    """KeyPairDesc - 密钥对信息，不包含私钥内容。"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "KeyPairFingerPrint": fields.Str(
            required=False, load_from="KeyPairFingerPrint"
        ),
        "KeyPairId": fields.Str(required=False, load_from="KeyPairId"),
        "KeyPairName": fields.Str(required=False, load_from="KeyPairName"),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
    }


class UHostTagSetSchema(schema.ResponseSchema):
    """UHostTagSet - DescribeUHostTags"""

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class PriceDetailSchema(schema.ResponseSchema):
    """PriceDetail - 价格详细信息"""

    fields = {
        "Snapshot": fields.Float(required=False, load_from="Snapshot"),
        "UDisk": fields.Float(required=False, load_from="UDisk"),
        "UHost": fields.Float(required=False, load_from="UHost"),
        "Volume": fields.Float(required=False, load_from="Volume"),
    }


class UHostPriceSetSchema(schema.ResponseSchema):
    """UHostPriceSet - 主机价格"""

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "ListPrice": fields.Float(required=False, load_from="ListPrice"),
        "ListPriceDetail": PriceDetailSchema(),
        "OriginalPrice": fields.Float(required=True, load_from="OriginalPrice"),
        "OriginalPriceDetail": PriceDetailSchema(),
        "Price": fields.Float(required=True, load_from="Price"),
        "PriceDetail": PriceDetailSchema(),
    }


class BasePriceSetSchema(schema.ResponseSchema):
    """BasePriceSet - 价格信息"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "OriginalPrice": fields.Float(
            required=False, load_from="OriginalPrice"
        ),
        "Price": fields.Float(required=False, load_from="Price"),
    }
