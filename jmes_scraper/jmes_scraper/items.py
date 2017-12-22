"""JMES Scraper Items."""
# -*- coding: utf-8 -*-
import scrapy


class UserItem(scrapy.Item):
    """User item definition for jsonplaceholder /users endpoint."""
    user_id = scrapy.Field()  # id of the user
    name = scrapy.Field()  # name of the user
    email = scrapy.Field()  # email of the user
    address = scrapy.Field()  # list of aggregated address of the user
    phone = scrapy.Field()  # phone number of the user
    company = scrapy.Field()  # company name of the user
