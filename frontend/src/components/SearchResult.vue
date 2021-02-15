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

    <div class="post">
      <div class="loading" v-if="loading">
        Loading...
      </div>
    </div>

    <v-content v-if="post">
      <v-container>
        <h2 class="text-center">~検索結果~</h2>
        <v-conteiner fluid>
          <v-list two-line>
            <v-list-item  v-for="music in data" v-bind:key="music.music_name" @click="goChangeMusic(music.id, search_key, search_way, text)">
              <v-list-item-title>{{music.music_name}}</v-list-item-title>
              <v-list-item-subtitle>{{music.artist}}</v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-conteiner>
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from 'axios'
import config from '../../inc/config';

export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: null,
    data: [],
    loading: false,
    post: null,
    id: 0,
    text: '',
    search_key: '',
    search_way: ''
  }),
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      this.loading = true
      this.post = null
      const path = config.PASS + '/model/search'
      const params = new URLSearchParams()

      params.append('text', this.$route.params.text)
      params.append('search_key', this.$route.params.key)
      params.append('search_way', this.$route.params.way)
      
      this.text = this.$route.params.text
      this.search_key = this.$route.params.key
      this.search_way = this.$route.params.way

      axios.post(path, params).then(res => {
        this.data = res.data.result
        this.loading = false
        this.post = res.data
      }).catch(e => {
        console.log(e)
      })
    },
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
    goChangeMusic (id, key, way, text) {
      this.$router.push({name: 'ChangeMusic', params: { id: id, key: key, way: way, text: text }})
    }
  }
}
</script>
