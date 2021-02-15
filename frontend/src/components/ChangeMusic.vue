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
        <h2 class="text-center">曲確認・編集</h2>

        <div>
          <v-btn large color="normal" @click="backSearchResult()">戻る</v-btn>
        <div>

        <v-row>
          <v-col cols="12" sm="6" md="3">
            <v-text-field label="曲タイトル" oulined v-model="music_name"></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="3">
            <v-text-field label="曲タイトル(ひらがな)" oulined v-model="music_name_hiragana"></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="3">
            <v-text-field label="アーティスト" oulined v-model="artist"></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-subheader class="pl-0">キー</v-subheader>
            <v-slider v-model="key" thumb-label="always" max="6" min="-6"></v-slider>
          </v-col>
        </v-row>

        <v-dialog v-model="change_dialog" persistent max-width="290" dark="true">
          <template v-slot:activator="{ on }">
            <v-btn large color="primary" @click="sendMusicData()">変更ほじょん!</v-btn>
          </template>
          <v-cord>
            <v-card-title class="headline text-center">結果</v-card-title>
            <v-card-text v-if="result_message == 'OK'" class="text-center">保存完了！</v-card-text>
            <v-card-text v-if="result_message == 'NG'" class="text-center">未記入項目あり！"曲タイトル"と"アーティスト"にはなんか入れよう！</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="change_dialog = false">了解</v-btn>
            </v-card-actions>
          </v-cord>
        </v-dialog>

        <v-dialog v-model="delete_dialog" persistent max-width="290" dark="true">
          <v-cord>
            <v-card-title class="headline text-center">結果</v-card-title>
            <v-card-text class="text-center">削除完了！</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="delete_dialog = false; goSearch()">了解</v-btn>
            </v-card-actions>
          </v-cord>
        </v-dialog>

        <v-dialog v-model="check_dialog" parsistent max-width="290" dark="true">
          <template v-slot:activator="{ on }">
            <v-btn large color="error" @click="check_dialog = true">さくじょ!</v-btn>
          </template>
          <v-card>
            <v-card-title class="headline text-center">確認！</v-card-title>
            <v-card-text class="text-center">ほんとに削除する？</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="check_dialog = false; deleteMusicData()">する！</v-btn>
              <v-btn text @click="check_dialog = false">しない...</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

      </v-container>
    </v-content>
    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: null,
    id: 0,
    music_name: '',
    music_name_hiragana: '',
    artist: '',
    key: 0,
    change_dialog: false,
    delete_dialog: false,
    check_dialog: false,
    result_message: 'OK',
    loading: false,
    post: null
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
      const path = 'dummy_url'
      const params = new URLSearchParams()

      params.append('id', this.$route.params.id)

      axios.post(path, params).then(res => {
        const data = res.data.result

        if (data.music_name === null || data.music_name === '') {
          return
        }

        this.id = data.id
        this.music_name = data.music_name
        this.music_name_hiragana = data.music_name_hiragana
        this.artist = data.artist
        this.key = data.key

        this.loading = false
        this.post = res.data
      }).catch(e => {
        console.log(e)
      })
    },
    backSearchResult () {
      this.$router.push({ name: 'SearchResult', params: { key: this.$route.params.key, way: this.$route.params.way, text: this.$route.params.text }})
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
    sendMusicData () {
      const path = 'https://karaoke-my-edit-web-app.herokuapp.com/model/change'
      const params = new URLSearchParams()

      if (this.music_name === '' ||
        this.artist === '') {
        this.result_message = 'NG'
        this.change_dialog = true
        return
      }

      params.append('id', this.id)
      params.append('music_name', this.music_name)
      params.append('music_name_hiragana', this.music_name_hiragana)
      params.append('artist', this.artist)
      params.append('key', this.key)

      axios.post(path, params).then(res => {
        this.result_message = 'OK'
        this.change_dialog = true
      }).catch(e => {
        console.log(e)
      })
    },
    deleteMusicData () {
      const path = 'https://karaoke-my-edit-web-app.herokuapp.com/model/delete'
      const params = new URLSearchParams()

      params.append('id', this.id)

      axios.post(path, params).then(res => {
        this.result_message = 'OK'
        this.delete_dialog = true
      }).catch(e => {
        console.log(e)
      })
    }
  }
}
</script>
