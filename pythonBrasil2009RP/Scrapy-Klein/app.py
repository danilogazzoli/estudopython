from klein import Klein
from scrapy.utils.serialize import ScrapyJSONEncoder
import json
import app
from spider_runner import SpiderRunner
from tutorial.tutorial.spiders.quotes_spider import QuotesSpider

app = Klein()

@app.route("/")
def index(request):
    return "Bom dia, daqui a pouco tem almoço"

@app.route('/search')
def get_quotes(request):
    content = json.loads(request.content.read())
    tag = content.get("tag")
   
    runner = SpiderRunner()

    deferred = runner.crawl(QuotesSpider, tag=tag)
    deferred.addCallback(return_spider_output)

    return deferred

def return_spider_output(output):
    _encoder = ScrapyJSONEncoder(ensure_ascii=False)
    return _encoder.encode(output)


app.run("localhost", 8080)

