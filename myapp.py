from source.myserver import *

app = server()
app.run(host="localhost", port=3000, debug=True)