# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# update_time: year-month-day[更新时间一律精确到天]

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class MedicalmapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MedicalMapLoader(ItemLoader):
    default_output_processor = TakeFirst()


class HospitalInfoItem(scrapy.Item):
    """
    医院信息表
    hospital_name       医院名称
    consulting_hour     医院上班时间
    hospital_level      医院等级 二级甲等,二级乙等,二级丙等,三级甲等,三级乙等,三级丙等,一级甲等,一级丙等,一级乙等,未定级
    hospital_type       医院性质 公立 私立
    hospital_category   医院分类 综合医院,中医医院,专科医院,妇幼保健院,卫生服务中心,卫生院,疾病预防控制中心
    hospital_addr       医院地址
    hospital_pro        医院所属省
    hospital_city       医院所属市
    hospital_county     医院所属县
    hospital_phone      医院电话
    hospital_intro      医院简介
    is_medicare         是否接入医保
    medicare_type       医保类型
    vaccine_name        疫苗类型
    is_cpc              是否有胸痛中心
    is_bdc              是否有脑卒中中心
    cooperative_business和微医平台的合作业务
    hospital_district   院区
    registered_channel  挂号渠道
    update_time             更新时间
    """
    hospital_name = scrapy.Field()
    consulting_hour = scrapy.Field()
    hospital_level = scrapy.Field()
    hospital_type = scrapy.Field()
    hospital_category = scrapy.Field()
    hospital_addr = scrapy.Field()
    hospital_pro = scrapy.Field()
    hospital_city = scrapy.Field()
    hospital_county = scrapy.Field()
    hospital_phone = scrapy.Field()
    hospital_intro = scrapy.Field()
    is_medicare = scrapy.Field()
    medicare_type = scrapy.Field()
    vaccine_name = scrapy.Field()
    is_cpc = scrapy.Field()
    is_bdc = scrapy.Field()
    cooperative_business = scrapy.Field()
    hospital_district = scrapy.Field()
    registered_channel = scrapy.Field()
    dataSource_from = scrapy.Field()
    update_time = scrapy.Field()

    def get_sql_info(self):
        insert_sql = "insert into hospital_info(hospital_name,consulting_hour,hospital_level,hospital_type," \
                     "hospital_category,hospital_addr,hospital_pro,hospital_city,hospital_county,hospital_phone," \
                     "hospital_intro,is_medicare,medicare_type,vaccine_name,is_cpc,is_bdc,cooperative_business," \
                     "hospital_district,registered_channel,dataSource_from,update_time) " \
                     "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                     "on duplicate key update update_time=values(update_time)"
        params = [
            self['hospital_name'],
            self['consulting_hour'],
            self['hospital_level'],
            self['hospital_type'],
            self['hospital_category'],
            self['hospital_addr'],
            self['hospital_pro'],
            self['hospital_city'],
            self['hospital_county'],
            self['hospital_phone'],
            self['hospital_intro'],
            self['is_medicare'],
            self['medicare_type'],
            self['vaccine_name'],
            self['is_cpc'],
            self['is_bdc'],
            self['cooperative_business'],
            self['hospital_district'],
            self['registered_channel'],
            self['dataSource_from'],
            self['update_time'],
        ]
        return insert_sql, params


class HospitalDepItem(scrapy.Item):
    """
    科室信息表
    hospital_id     医院ID
    dept_type        科室类别 一级科室名称
    dept_name        科室名称 二级科室名称
    dep_intro       科室介绍
    update_time         更新时间
    """
    dept_name = scrapy.Field()
    hospital_name = scrapy.Field()
    dept_type = scrapy.Field()
    dept_intro = scrapy.Field()
    update_time = scrapy.Field()


class DoctorInfoItem(scrapy.Item):
    """
    医生信息表
    doctor_name     医生姓名
    sex             医生性别
    hospital_id     所属医院
    dep_id          所属科室
    doctor_level    医生等级
    doctor_intro    医生简称
    doctor_goodAt   医生擅长
    diagnosis_amt   医生诊疗费用
    update_time         更新时间
    """
    doctor_name = scrapy.Field()
    dept_name = scrapy.Field()
    hospital_name = scrapy.Field()
    sex = scrapy.Field()
    doctor_level = scrapy.Field()
    doctor_intro = scrapy.Field()
    doctor_goodAt = scrapy.Field()
    diagnosis_amt = scrapy.Field()
    update_time = scrapy.Field()


class DoctorRegInfoItem(scrapy.Item):
    """
    医生排班信息表
    doctor_name     医生名称
    hospital_name   所属医院名称
    dept_name       科室名称
    reg_info        排班信息
    update_time     更新时间
    """
    doctor_name = scrapy.Field()
    hospital_name = scrapy.Field()
    dept_name = scrapy.Field()
    reg_info = scrapy.Field()
    update_time = scrapy.Field()
