<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat>
      <v-container class="py-0 fill-height">
        <v-btn text @click="$router.push({ path: '/' })">
          <v-icon>mdi-home</v-icon>
          Home
        </v-btn>
        <v-btn text @click="$router.push('Authors')">
          <v-icon>mdi-account-edit</v-icon>
          Authors
        </v-btn>
        <v-btn text @click="$router.push('worksofart')">
          <v-icon>mdi-book-multiple</v-icon>Works of Art
        </v-btn>

        <v-spacer></v-spacer>

        <!--        <v-responsive max-width="260">-->
        <!--          <v-text-field-->
        <!--            dense-->
        <!--            flat-->
        <!--            hide-details-->
        <!--            rounded-->
        <!--            solo-inverted-->
        <!--          ></v-text-field>-->
        <!--        </v-responsive>-->
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item v-for="n in 5" :key="n" link>
                  <v-list-item-content>
                    <v-list-item-title> List Item {{ n }} </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item link color="grey lighten-4">
                  <v-list-item-content>
                    <v-list-item-title>
                      Refresh
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet min-height="70vh" rounded="lg">
              <router-view></router-view>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    links: ["Authors", "Works of Art"]
  })
};
</script>
