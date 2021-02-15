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
      <v-container>
        <h2 class="text-center">曲検索！</h2>

        <h4 class="text-center">検索の種類</h4>
        <v-conteiner fluid>
          <v-radio-group v-model="search_key" :mandatory="false">
            <v-radio label="曲名" value="music"></v-radio>
            <v-radio label="アーティスト" value="artist"></v-radio>
          </v-radio-group>
        </v-conteiner>

        <h4 class="text-center">検索の方法</h4>
        <v-conteiner fluid>
          <v-radio-group v-model="search_way" :mandatory="false">
            <v-radio label="から始まる" value="start"></v-radio>
            <v-radio label="を含む" value="include"></v-radio>
          </v-radio-group>
        </v-conteiner>

        <v-row>
          <v-col cols="12" sm="6" md="3">
            <v-text-field label="てきすと" filled v-model="text"></v-text-field>
          </v-col>
        </v-row>

        <div class="text-center my-2">
          <v-btn large block color="primary" @click="goSearchResult()">けんさく!</v-btn>
        </div>
        <div class="text-center my-2">
          <v-btn large block color="normal" @click="goAllSearchResult()">全部けんさく!</v-btn>
        </div>
        <div class="text-center my-2">
          <v-btn large block color="normal" @click="goRandomSearchResult()">ランダムけんさく!</v-btn>
        </div>

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
    drawer: null,
    search_key: 'music',
    search_way: 'start',
    text: ''
  }),
  methods: {
    goTop () {
      this.$router.push({ name: 'Top' })
    },
    goSearch () {
      this.$router.push({ name: 'Search' })
    },
    goAddMusic () {
      this.$router.push({ name: 'AddMusic' })
    },
    goSetting () {
      this.$router.push({ name: 'Setting' })
    },
    goSearchResult () {
      if (this.text === '' ){
        this.text = ';'
      }
      this.$router.push({ name: 'SearchResult', params: { key: this.search_key, way: this.search_way, text: this.text }})
    },
    goAllSearchResult () {
      this.$router.push({ name: 'SearchResult', params: { key: this.search_key, way: this.search_way, text: ';' }})
    },
    goRandomSearchResult () {
      this.$router.push({ name: 'SearchResult', params: { key: this.search_key, way: this.search_way, text: 'rand;' }})
    }
  }
}
</script>
