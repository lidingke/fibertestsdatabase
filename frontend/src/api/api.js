import axios from 'axios';
let local_host = "http://127.0.0.1:8000"

// export const getinit = params =>{
    // return axios.get(`${local_host}/producer/`);
// }

export const getinit = params => { return axios.get(`${local_host}/producer/`) }

// export const getcolumn = params => { return axios.get(`${local_host}/producercolumns/`) }

export const login = params => {
    return axios.post(`${local_host}/login/`, params)
  }