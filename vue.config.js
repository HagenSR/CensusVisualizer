module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? 'https://hagensr.github.io/CensusVisualizer/'
    : '/',
  "devServer": {
    "proxy": "https://us-central1-oval-proxy-276213.cloudfunctions.net/"
  },
  "transpileDependencies": [
    "vuetify"
  ]
}