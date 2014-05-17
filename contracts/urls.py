from django.conf.urls import patterns, url, include
from django.utils.translation import ugettext_lazy as _

from . import feed
from . import views

from . import entity_urls
from . import contract_urls
from . import category_urls
from . import analysis_urls


urlpatterns = patterns('',
                       url(r'^%s/%s$' % (_('contracts'), _('home')), views.home, name='contracts_home'),
                       url(r'^%s$' % _('analysis'), views.analysis, name='contracts_analysis'),

                       url(r'^%s$' % _('contracts'), views.contracts_list, name='contracts_list'),
                       url(r'^%s/rss$' % _('contracts'), feed.ContractsFeed(), name='contracts_list_feed'),

                       url(r'^%s$' % _('categories'), views.categories_list, name='categories_list'),

                       url(r'^%s$' % _('tenders'), views.tenders_list, name='tenders_list'),
                       url(r'^%s/rss$' % _('tenders'), feed.TendersFeed(), name='tenders_list_feed'),

                       url(r'%s/' % _('analysis'), include(analysis_urls)),

                       url(r'^%s$' % _('entities'), views.entities_list, name='entities_list'),

                       url(r'%s/' % _('contract'), include(contract_urls)),

                       url(r'%s/' % _('entity'), include(entity_urls)),

                       url(r'%s/' % _('category'), include(category_urls)),
)
