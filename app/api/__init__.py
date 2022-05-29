from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

#MOVIES
from app.api.movies.get_movies_list import get_movies_list

#USERS
from app.api.users.create_user import create_user
from app.api.users.delete_user import delete_user
from app.api.users.update_user import updated_user
from app.api.users.list_user import list_users
from app.api.users.user_detail import detail_user


#WATCHLIST
from app.api.watchlist.create_watchlist import create_watchlist
from app.api.watchlist.update_watchlist import update_watchlist
from app.api.watchlist.delete_watchlist import delete_watchlist
from app.api.watchlist.get_watchlist import list_watchlist
from app.api.watchlist.get_watchlist_per_user import get_watchlist_per_user

def alive():
    return 'alive'


router = APIRouter()

router.add_api_route('/alive', endpoint=alive, tags=['Status'], response_class=PlainTextResponse)

# Movie
router.add_api_route('/movies/list', endpoint=get_movies_list, methods=['GET'], tags=['Movies'])

# Users
router.add_api_route('/user/create', endpoint=create_user, methods=['POST'], tags=['Users'])
router.add_api_route('/user/update/{user_id}', endpoint=updated_user, methods=['PUT'], tags=['Users'])
router.add_api_route('/user/delete/{user_id}', endpoint=delete_user, methods=['DELETE'], tags=['Users'])
router.add_api_route('/user/list', endpoint=list_users, methods=['GET'], tags=['Users'])
router.add_api_route('/user/{user_id}', endpoint=detail_user, methods=['GET'], tags=['Users'])

# Watchlist
router.add_api_route('/watchlist/create/{user_id}', endpoint=create_watchlist, methods=['POST'], tags=['Watchlist'])
router.add_api_route('/watchlist/update/{user_id}', endpoint=update_watchlist, methods=['PUT'], tags=['Watchlist'])
router.add_api_route('/watchlist/delete/{user_id}/{movie_id}', endpoint=delete_watchlist, methods=['DELETE'], tags=['Watchlist'])
router.add_api_route('/watchlist/list', endpoint=list_watchlist, methods=['GET'], tags=['Watchlist'])
router.add_api_route('/watchlist/list/{user_id}', endpoint=get_watchlist_per_user, methods=['GET'], tags=['Watchlist'])


