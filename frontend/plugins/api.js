import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const config = {
  headers: {'Access-Control-Allow-Origin': '*'}
};

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

// TODO: obter baseURL das variáveis de ambiente
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

function remove(url)
{
  return axios.delete(baseURL + url);
}
