import axios from 'axios'

const service = axios.create({
    baseURL: 'http://localhost:5000',
    timeout: 5000
})

class CifradorApi {
    constructor (){}
    
    async cifrar(data) {
        return await service.post('/cifrar', data);
    }
    
    async decifrar(data) {
        return await service.post('/decifrar', data);
    }

}

export default new CifradorApi();