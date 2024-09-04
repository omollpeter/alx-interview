#!/usr/bin/node

const request = require('request');

// request("https://swapi-api.alx-tools.com/api/films/1/", (error, response, body) => {
//     if (error) {
//         console.error("Error occurred:", error);
//         return;
//     }
//     const data = JSON.parse(body);
//     console.log(data.characters);
// })

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}

async function getData (url, movieId) {
  try {
    const data = await requestPromise(url + movieId);
    const jsonData = await JSON.parse(data);

    const characters = jsonData.characters;
    for (let i = 0; i < characters.length; i++) {
      const charDetails = await requestPromise(characters[i]);
      const jsonCharDetails = await JSON.parse(charDetails);
      const charName = jsonCharDetails.name;
      console.log(charName);
    }
  } catch (error) {
    console.error('Error occurred:', error);
  }
}

getData('https://swapi-api.alx-tools.com/api/films/', process.argv[2]);
