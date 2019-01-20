module.exports = {
    devServer: {
        proxy: {
            '/websocket': {
                target: 'http://localhost:8080',
                ws: true,
                changeOrigin: true
            }
        }
    }
}