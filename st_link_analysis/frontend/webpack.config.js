const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CopyPlugin = require("copy-webpack-plugin");
const BundleAnalyzerPlugin = require("webpack-bundle-analyzer").BundleAnalyzerPlugin;

var config = {
    entry: {
        index: "./src/index.js",
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html",
            minify: {
                collapseWhitespace: true,
                removeComments: true,
            },
        }),
        new CopyPlugin({
            patterns: [{ from: "./src/assets/icons", to: "icons" }],
        }),
    ],
    output: {
        filename: "[name].[contenthash].bundle.js",
        path: path.resolve(__dirname, "build"),
        clean: true,
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: "asset/resource",
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: "asset/resource",
            },
        ],
    },
};

module.exports = (env, argv) => {
    if (argv.mode == "development") {
        config.devtool = "inline-source-map";
        config.devServer = {
            static: "./build",
            port: 3001,
            compress: true,
        };
        config.optimization = {
            runtimeChunk: "single",
            splitChunks: {
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: "vendors",
                        chunks: "all",
                    },
                },
            },
        };
    } else if (argv.mode == "production") {
        config.optimization = {
            runtimeChunk: "single",
            splitChunks: {
                chunks: "all",
                cacheGroups: {
                    streamlit: {
                        test: /[\\/]node_modules[\\/]streamlit-component-lib/,
                        name: "streamlit-component-lib",
                        chunks: "all",
                    },
                    cyotscape: {
                        test: /[\\/]node_modules[\\/]cytoscape/,
                        name: "cytoscape",
                        chunks: "all",
                    },
                    apache_arrow: {
                        test: /[\\/]node_modules[\\/]apache-arrow/,
                        name: "apache-arrow",
                        chunks: "all",
                    },
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: "vendors",
                        chunks: "all",
                        enforce: true,
                    },
                },
            },
        };
    }
    return config;
};
