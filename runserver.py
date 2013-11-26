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
Import Application Dependencies

Import the appropriate methods to initialize the application in compliance
with the Application Factory method, of which further documentation can be
found at http://flask.pocoo.org/docs/patterns/appfactories/

"""
import os, sys
from commonscloudproxy import create_application

"""
Start the application

Ensure that the virtual environment has been properly activated and if it
has been, then the application should be run, using the initialize_application
method provided so comply with the Application Factory pattern

"""
if __name__ == "__main__":
  if "VIRTUAL_ENV" not in os.environ:
    print("""
    Your Virtual Environment or virtualenv has not been activated.

    To use this application, please activate it by executing:
    
      source venv/bin/activate
      
    If the problem persists, ensure that virtualenv is installed:
    
      pip install virtualenv
      
    and that all other requirements have been satisfied.
    """)
  elif len(sys.argv) > 1 and sys.argv[1] == "development":
    commonscloudproxy = create_application(__name__, env='settings_development')
    commonscloudproxy.run()
  elif len(sys.argv) > 1 and sys.argv[1] == "production":
    commonscloudproxy = create_application(__name__, env='settings_production')
    commonscloudproxy.run()
  else:
    commonscloudproxy = create_application(__name__)
    commonscloudproxy.run()