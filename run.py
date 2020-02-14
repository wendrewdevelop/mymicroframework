from core import Framework
from core.template import Template


framework = Framework()
view = Template()

@framework.route("/")
def index():
    context = {
        "name": "Wendrew"
    }
    
    return view.render("index.html", context)


if __name__ == "__main__":
    framework.run(port=4000, reloader=True)