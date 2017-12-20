import axios from 'axios';
let local_host = "http://127.0.0.1:8080"

// export const getinit = params =>{
    // return axios.get(`${local_host}/producer/`);
// }

export const getinit = params => { return axios.get(`${local_host}/producer/`) }

export const getcolumn = params => { return axios.get(`${local_host}/producercolumns/`) }
