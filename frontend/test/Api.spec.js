import api from '~/plugins/api'

describe('Test API', () => {
  it('Testing api/register/list', async() => {
    const response = await api.list('api/register/list');
    expect(response.status).toBe(200);
    expect(response.headers['content-type']).toBe('application/json')
  })
})
