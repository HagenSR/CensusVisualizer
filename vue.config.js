module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? 'http://students.cs.ndsu.nodak.edu/~seahagen/Census/'
    : '/',
  "devServer": {
    "proxy": "https://us-central1-oval-proxy-276213.cloudfunctions.net/"
  },
  "transpileDependencies": [
    "vuetify"
  ]
}