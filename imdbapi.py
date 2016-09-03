from database import Show, Episode, Stats, init_db
from bottle import route, run, request, template, response
import simplejson
import sqlalchemy
import urllib

session = init_db()

def get_data(show_name, show_year=None):
    if not show_name or (show_year and not show_year.isdigit()):
        return None

    show = session.query(Show).filter(Show.name.like(show_name))
    if show_year:
        show = show.filter(Show.year==int(show_year))
    try:
        single_show = show.one()
    except sqlalchemy.orm.exc.NoResultFound:
        return None
    except sqlalchemy.orm.exc.MultipleResultsFound:
        shows = show.order_by(Show.name)[:15]
        show_list = [{"name": show.name, "year": show.year} for show in shows]
        return {"shows": show_list}

    episodes = []
    for episode in single_show.episodes:
        episodes.append({"name": episode.name, "number": episode.number, "season": episode.season})
    return {single_show.name: {"year": single_show.year, "episodes": episodes}}

@route('/json/')
def json():
    response.content_type = 'application/json'
    show_name = request.GET.get("name", None)
    show_year = request.GET.get("year", None)
    callback = request.GET.get("callback", None)
    data = simplejson.dumps(get_data(show_name, show_year))
    session.close()
    if callback:
        data = "%s(%s)" % (callback, data)
    return data

@route('/js/')
def js():
    show_name = request.GET.get("name", None)
    show_year = request.GET.get("year", None)
    callback = request.GET.get("callback", None)
    data = simplejson.dumps(get_data(show_name, show_year))
    session.close()
    if callback:
        data = "%s(%s)" % (callback, data)
    return data

@route('/')
def index():
    return template("index")

if __name__ == "__main__":
    run(host='localhost', port=8000)
