module.exports = {
    moduleNameMapper: {
      '^vue$': 'vue/dist/vue.common.js',
      'vuetify/lib(.*)': '<rootDir>/node_modules/vuetify/es5$1',
    },
    moduleFileExtensions: ['js', 'vue'],
    modulePaths: ['<rootDir>/src', '<rootDir>/node_modules'],
    transform: {
      '.+\\.(css|styl|less|sass|scss|png|jpg|ttf|woff|woff2)$':
        'jest-transform-stub',
      '^.+\\.js$': ['<rootDir>/node_modules/babel-jest'],
      '.*\\.(vue)$': ['<rootDir>/node_modules/vue-jest'],
    },
    transformIgnorePatterns: ['<rootDir>/node_modules/(?!(vuetify)/)'],
    setupFiles: ['<rootDir>/test/index.js'],
    collectCoverageFrom: ['<rootDir>/src/**/*.{js,vue}'],
};
  