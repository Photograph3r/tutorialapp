urlpatterns = patterns('',
	#Examples:
	#url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
	#url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('tutorial_app.urls')), # ADD THIS NEW TUPLE!
)