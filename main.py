from journal import Journal
from journal_manage import JournalMangaement

jour = Journal("./test_data/sample1.pdf")
jour.read_text()

jour.check_data_type()
if jour.data != "image" :
    jour.image_to_text()    
if jour.data_clensing_front() :
    jour.data_clensing_back()
    
print(jour.data)