import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

let baseURL = '';

// TODO: needs to improve
if(window.location.href !== 'http://localhost/'){
  baseURL = 'API_URL'
}

console.log(baseURL)

const api = {
  list(url,data){
    return get(url,data);
  },
  create(url,data){
    return post(url,data);
  },
  update(url,data){
    return post(url,data);
  },
  remove(url){
    return remove(url);
  }
};

export default api

function get(url, params){
  return axios.get(baseURL + url, {params: params});
}

function post(url, params){
  var fd = new FormData();
  params = params || {}
  Object.keys(params).map((k) => {
      fd.append(k, params[k]);
  })
  return axios.post(baseURL + url, fd);
}

function remove(url)
{
  return axios.delete(baseURL + url);
}
