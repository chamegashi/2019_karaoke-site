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
        <h2 class="text-center">曲ついか</h2>
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
        <v-dialog v-model="dialog" persistent max-width="290" dark="true">
          <template v-slot:activator="{ on }">
            <v-btn large block color="primary" @click="sendMusicData()">ほじょん!</v-btn>
          </template>
          <v-cord>
            <v-card-title class="headline text-center">結果</v-card-title>
            <v-card-text v-if="result_message == 'OK'" class="text-center">保存完了！</v-card-text>
            <v-card-text v-if="result_message == 'NG'" class="text-center">未記入項目あり！"曲タイトル"と"アーティスト"にはなんか入れよう！</v-card-text>
            <v-card-text v-if="result_message == 'SAME'" class="text-center">同じデータがすでにあるよー</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="dialog = false">了解</v-btn>
            </v-card-actions>
          </v-cord>
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
    music_name: '',
    music_name_hiragana: '',
    artist: '',
    key: 0,
    dialog: false,
    result_message: 'OK'
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
    sendMusicData () {
      const path = 'dummy_url'
      const params = new URLSearchParams()

      if (this.music_name === '' ||
        this.artist === '') {
        this.result_message = 'NG'
        this.dialog = true
        return
      }

      params.append('music_name', this.music_name)
      params.append('music_name_hiragana', this.music_name_hiragana)
      params.append('artist', this.artist)
      params.append('key', this.key)

      axios.post(path, params).then(res => {
        if (res.data.responce === "same") {
          this.result_message = 'SAME'
          this.dialog = true
        }
        this.music_name = ''
        this.music_name_hiragana = ''
        this.artist = ''
        this.key = 0
        this.result_message = 'OK'
        this.dialog = true
      }).catch(e => {
        console.log(e)
      })
    }
  }
}
</script>
