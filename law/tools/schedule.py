"""
Module run every day by a cron job to update database
and cache.
"""
## setup the Django with its private settings for server.
import set_up
set_up.set_up_django_environment('settings_private')

from law.crawler import FirstSeriesCrawler

crawler = FirstSeriesCrawler()

crawler.extract_law_types()
crawler.save_all_summaries()