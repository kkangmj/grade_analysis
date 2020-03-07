const {createProxyMiddleware} = require('http-proxy-middleware');

const apiUrl = 'http://localhost:8000';

const apiContext = ['/api'];

module.exports = function (app) {
    app.use(
        createProxyMiddleware(
            apiContext, {
            target: apiUrl,
            changeOrigin: true
        })
    )
};