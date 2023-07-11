from journal import Journal
from journal_manage import JournalMangaement
from config import *

ai_key = OPENAI_KEY
path = PATH
model = "gpt-3.5-turbo"
jour_manage = JournalMangaement(ai_key, model ,path)

jour_manage.set_journal_list()
jour_manage.run_ai()