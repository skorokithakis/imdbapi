from __future__ import with_statement
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref
from database import Show, Episode, init_db

import codecs
import re
import sqlalchemy

session = init_db(transactional=True)

def import_data(filename):
    """Import episode names and ratings from a file."""
    regex = re.compile(""""(?P<show_name>.*?)"\s+\((?P<year>\d+)(?:|/.*?)\)\s+\{(?P<episode_name>.*?) \(\#(?P<season_no>\d+)\.(?P<episode_no>\d+)\)\}""")
    with codecs.open(filename, "r", "latin-1") as ratings:
        # Generate all the lines that matched.
        matches = (match for match in (regex.search(line.strip()) for line in ratings) if match)
        counter = 0
        for match in matches:
            counter += 1
            if not counter % 100:
                print counter
            episode = {}
            for field in ["show_name", "year", "episode_name", "episode_no", "season_no"]:
                episode[field] = match.group(field)

            try:
                show = session.query(Show).filter_by(name=episode["show_name"], year=episode["year"]).one()
            except sqlalchemy.orm.exc.NoResultFound:
                show = Show(episode["show_name"], episode["year"])
                session.add(show)

            try:
                episode = session.query(Episode).filter_by(name=episode["episode_name"], show=show).one()
            except sqlalchemy.orm.exc.NoResultFound:
                episode = Episode(show, episode["episode_name"], episode["season_no"], episode["episode_no"])
                session.add(episode)

    #session.commit()

if __name__ == "__main__":
    import_data("movies.list")

