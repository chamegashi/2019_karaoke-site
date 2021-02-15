import Vue from 'vue'
import Router from 'vue-router'
import Top from '@/components/Top'
import Search from '@/components/Search'
import AddMusic from '@/components/AddMusic'
import Setting from '@/components/Setting'
import SearchResult from '@/components/SearchResult'
import ChangeMusic from '@/components/ChangeMusic'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Top',
      component: Top
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/addmusic',
      name: 'AddMusic',
      component: AddMusic
    },
    {
      path: '/setting',
      name: 'Setting',
      component: Setting
    },
    {
      path: '/searchresult/:key/:way/:text',
      name: 'SearchResult',
      component: SearchResult
    },
    {
      path: '/chengemusic/:id/:key/:way/:text',
      name: 'ChangeMusic',
      component: ChangeMusic
    }
  ]
})
