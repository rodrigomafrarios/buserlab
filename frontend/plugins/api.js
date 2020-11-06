import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const config = {
  headers: {'Access-Control-Allow-Origin': '*'}
};

const api = {
  list(url,data){
    return get(url,data);
  }
};

const baseURL = 'http://localhost/'

export default api

function get(url, params){
  return axios.get(baseURL + url, {params: params},config);
}

function post(url, params){
  var fd = new FormData();
  params = params || {}
  Object.keys(params).map((k) => {
      fd.append(k, params[k]);
  })
  return axios.post(baseURL + url, fd,config);
}
