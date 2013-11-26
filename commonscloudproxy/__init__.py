"""
For CommonsCloudProxy copyright information please see the License document included with
this software package.

Licensing information can be found in the LICENSE document (the "License")
included with this copy of the software and this file may not be used in any
manner except in compliance with the License

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""


"""
Import System dependencies
"""
import requests
from urlparse import urlparse

"""
Import Flask dependencies
"""
from flask import Flask
from flask import json
from flask import jsonify
from flask import request


"""
Setup our base Flask application, retaining it as our application
object for use throughout the application
"""
def create_application(name = __name__, env = 'settings_testing'):
    
    app = Flask(__name__, static_path = '/static')

    # Load our default configuration
    load_configuration(app, env)
    
    # Load default application routes/paths
    basic_routing(app)

    return app


"""
Load the basic configuration settings for our application from
another file that holds all of our default settings. All Flask
and Flask Extension defaults/configuration handling should be
placed in the this 'settings.py' folder in the application root.
"""
def load_configuration(app, environment):
    app.config.from_object(__name__)
    app.config.from_object('settings_default')
    app.config.from_object(environment)



"""
Setup some basic routes to get our application started, even if all
we're showing folks is a 404, 500, or the home page.
"""
def basic_routing(app):

  
  """
  The Application Index gives us a route to the "homepage" of our application. Currently
  this takes you to the Application Dashboard, but in the future I sould see the index or
  www.commonscloud.org going to a sales home page and linking to other "sales" pages, versus
  just being associated with the application.
  """
  @app.route('/')
  def proxy_index():
  
    """
    Grab the url from the `url` parameter and pass it through the Python URL Parse tool
    """
    url_to_proxy   = request.args.get('url')
    clean_url      = urlparse(url_to_proxy)

    """
    Using the cleaned URL, we can pass it to our request method and get the contents of
    the page being requested
    """
    r = requests.get(clean_url.geturl())
    data = json.loads(r.content)
  
    """
    Build a response object to display pretty JSON for easy reading
    """
    results = jsonify(data)
    results.status_code = 200
    results.headers['Access-Control-Allow-Origin'] = '*'
  
    return results  