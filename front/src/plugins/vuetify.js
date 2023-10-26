import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'


export default createVuetify({
  icons: {
    defaultSet: 'mdi' // This is already the default value - only for display purposes
  },
  components,
  directives
})
// import '@mdi/font/css/materialdesignicons.css' // Make sure you are using css-loader
// import { createVuetify, VuetifyPreset } from 'vuetify' // Import appropriate types from vuetify
// import 'vuetify/styles'
// import * as components from 'vuetify/components'
// import * as directives from 'vuetify/directives'

// const vuetifyOptions: Partial<VuetifyPreset> = {
//   // Make sure to use the correct types for VuetifyPreset
//   icons: {
//     defaultSet: 'mdi' // This is already the default value, for display purposes only
//   },
//   components,
//   directives
// }

// export default createVuetify(vuetifyOptions)
