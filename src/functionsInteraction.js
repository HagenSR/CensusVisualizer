const axios = require('axios');


var getCoutry = function getCounty(count) {
  var url = 'https://us-central1-oval-proxy-276213.cloudfunctions.net/getCounty';
  return new Promise(function (res, fail) {
    axios.post(url, {
      county: count,
    })
      .then(function (response) {
        res(response.data);
      })
      .catch(function (error) {
        fail(error);
      });
  })

}

const getByID = async function getByID(id) {
  var url = 'https://us-central1-oval-proxy-276213.cloudfunctions.net/getCountByID';
  return new Promise(function (res, flnk) {
    axios.post(url, {
      ID: id,
    })
      .then(function (response) {
        res(response.data);
      })
      .catch(function (error) {
        flnk(error);
      });
  })
}

exports.getByID = getByID;
exports.getCounty = getCoutry;



