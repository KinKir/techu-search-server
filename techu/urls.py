from django.conf.urls import patterns, include, url

urlpatterns = patterns('techu.views',
  url(r'^configuration[/]*$', 'configuration', name = 'configuration_insert'),
  url(r'^configuration/list[/]*$', 'configuration_list', name = 'configuration_list'),
  url(r'^configuration/(?P<conf_id>\d+)[/]*$', 'configuration', name = 'configuration'),
  url(r'^option[/]*$', 'option', name = 'option_insert'),
  url(r'^option/list[/]*$', 'option_list', name = 'option_list'),
  url(r'^index[/]*$', 'index', name = 'index_insert'),
  url(r'^index/(?P<index_id>\d+)[/]*$', 'index', name = 'index'),
  url(r'^index/list[/]*$', 'index_list', name = 'index_list'),
  url(r'^indexer/(?P<action>[a-z]+)/(?P<index_id>\d+)/(?P<doc_id>\d+)[/]*$', 'indexer', name = 'indexer'),
  url(r'^search/(?P<index>[a-z0-9_])[/]*$', 'search', name = 'search'),
  url(r'^excerpts/(?P<index>[a-z0-9_])[/]*$', 'excerpts', name = 'excerpts'),
  url(r'^generate/(?P<configuration_id>\d+)[/]*$', 'generate', name = 'generate'),
  url(r'^batch/(?P<action>[a-z]+)/(?P<index_id>\d+)[/]*$', 'batch_indexer', name = 'batch_indexer'),
  url(r'^[/]*$', 'home', name = 'home'),
)

