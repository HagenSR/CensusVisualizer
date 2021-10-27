const axios = require('axios');
const qs = require('qs');

var getCoutry = function getCounty(count) {
<<<<<<< HEAD
  var url = 'https://census-api-sean.herokuapp.com/getStatesByName.php';
=======
  var url = 'https://census-api-sean.herokuapp.com/getCounties';
>>>>>>> af8cb1e65a159bafaf3444468de41cd59d5ffa8c
  count = count.substring(0, 1).toUpperCase() + count.substring(1, count.length).toLowerCase()
  return new Promise(function (res, fail) {
    axios.post(
      url,
      qs.stringify({county: count + "%"}))
      .then(function (response) {
        res(response.data);
      })
      .catch(function (error) {
        fail(error);
      });
  })

}

const getByID = async function getByID(id) {
<<<<<<< HEAD
  var url = 'https://census-api-sean.herokuapp.com/getState.php';
=======
  var url = 'https://census-api-sean.herokuapp.com/getCounty';
>>>>>>> af8cb1e65a159bafaf3444468de41cd59d5ffa8c
  console.log(id)
  if (!id || id == "" || isNaN(id)) {
    throw "ID was bad"
  } else {
    return new Promise(function (res, flnk) {
      axios.post(url, 
        qs.stringify({ID: id})
        )
        .then(function (response) {
          res(response.data);
        })
        .catch(function (error) {
          flnk(error);
        });
    })
  }

}

exports.getByID = getByID;
exports.getCounty = getCoutry;



