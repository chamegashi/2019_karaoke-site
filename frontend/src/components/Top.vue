<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item @click="goTop()">
          <v-list-item-action>
            <v-icon>menu_book</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>とっぷ</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="goSearch()">
          <v-list-item-action>
            <v-icon>search</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>曲検索</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="goAddMusic()">
          <v-list-item-action>
            <v-icon>library_add</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>曲の追加</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="goSetting()">
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>設定</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>曲用データベース(仮)</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <h1>おいでなすって！</h1>
          <p>左上のボタンから移動をどうぞー</p>
        </v-row>
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: null
  }),
  methods: {
    goTop () {
      this.$router.push({ path: '/' })
    },
    goSearch () {
      this.$router.push({ path: 'search' })
    },
    goAddMusic () {
      this.$router.push({ path: 'addmusic' })
    },
    goSetting () {
      this.$router.push({ path: 'setting' })
    }
  }
}
</script>
