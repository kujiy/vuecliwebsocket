module.exports = {
    devServer: {
        proxy: {
            '/websocket': {
                target: 'http://localhost:8081',
                ws: true,
                changeOrigin: true
            }
        }
    }
}