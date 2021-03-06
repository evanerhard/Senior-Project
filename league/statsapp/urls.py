from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register', views.register, name='register'),

    url(r'^drives/$', views.drives_list, name='drives_list'),
    url(r'^drives/(?P<drive_id>[a-zA-z--9]+)$', views.drive_view, name='drives'),

    url(r'^players/$', views.players_list, name='players_list'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/$', views.player_view, name='players'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/passing_yds_player/$', views.passing_yds_player, name='passing'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/rushing_yds_player/$', views.rushing_yds_player, name='rushing'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/receiving_yds_player/$', views.receiving_yds_player, name='receiving'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/sacks_player/$', views.sacks_player, name='sacks'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/tackles_player/$', views.tackles_player, name='tackles'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/picks_player/$', views.picks_player, name='picks'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/catches_player/$', views.catches_player, name='catches'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)/blocks_player/$', views.passblock_player, name='blocks'),


    url(r'^games/$', views.games_list, name='games_list'),
    url(r'^games/(?P<gsis_id>[a-zA-z--9]+)$', views.game_view, name='games'),

    url(r'^rookies/$', views.rookies_list, name='rookies_list'),

    url(r'^search/$', views.search_player, name='search_player'),
    url(r'^results/$', views.SearchResults.as_view(), name='search_results'),

    url(r'^compare/$', views.compare_players, name='compare_players'),


    url(r'^teams/$', views.teams_list, name='teams_list'),
    url(r'^teams/(?P<team_id>[a-zA-z--9]+)$', views.team_view, name='teams'),

    url(r'^top/$', views.five_qb_list, name='top'),

    url(r'^chart_example/$', views.chart_example, name='chart_example'),
]
