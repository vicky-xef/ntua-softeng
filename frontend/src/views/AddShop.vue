<template>
    <div id="add-shop">
      <b-jumbotron lead="Προσθήκη καταστήματος">
          <b-form @submit.prevent="post">
            <b-form-group 
               name="shopgroup"
                id="shopgroup" label="Όνομα καταστήματος:"
               label-cols =3  
               :invalid-feedback="errors.first('s_name')" >
              <b-form-input name="s_name" id="s_name" type="text"
                      v-validate="'required'"
                      data-vv-as="*Το όνομα"
                      v-model="shop.name" 
                      :state="errors.has('s_name') ? false :null" 
               />
            </b-form-group>  
             <b-form-group 
               id="tags" label="Ετικέτες:"
               label-for="s_tags" 
               label-cols =3 >
              <vue-tags-input 
                      name="s_tags" 
                      id="s_tags"
                      v-model= "shop.tag"     
                      placeholder= ""
                      :tags="shop.tags" 
                      @tags-changed="newTags => shop.tags = newTags"
              />
            </b-form-group>
            <b-form-group :state="errors.has('shop_loc') ? false :null" 
            :invalid-feedback="errors.first('shop_loc')" 
            id="mapgroup"
               label="Τοποθεσία"
                label-cols=3
              description="Hint: Πληκτρολόγησε την διεύθυνση του καταστήματος και αν θες μετακίνησε τον δείκτη στον χάρτη για μεγαλύτερη ακρίβεια στην τοποθεσία:">
             <myMap v-validate="'required'" data-vv-name="shop_loc" data-vv-as="*Η Τοποθεσία" @input="markerChanged" :with-geocoding="true" :with-location="true"></myMap>
              </b-form-group>
             <div class="spacer">
             <b-alert variant="success" v-model="err.suc" >ΕΠΙΤΥΧΙΑ</b-alert>
             <b-alert variant="danger" v-model="err.error">ΑΠΟΤΥΧΙΑ</b-alert>
             <b-button label-cols=1 type="submit" variant="primary">Προσθήκη</b-button>
             </div>
           </b-form>
        </b-jumbotron>
    </div>
</template>

<script>
import qs from 'qs';
import myMap from '../components/Map.vue'
export default {
  components:{
    'myMap': myMap
  },
  data() {
    return {
      shop:{
        name: '',
        address: '',
        tag: '',
        tags: [],
        lat: null,
        lng: null,
      },
      err:{
        error: null,
        suc: null
      }
    }
  },
  methods:{
    post: function(){
        this.$validator.validateAll().then(valid => {
            if (valid) {
                let empty_tags = (this.shop.tags.length == 0);
                this.$axios.post('/shops',
                    qs.stringify(
                        {
                            name: this.shop.name,
                            address: this.shop.address,
                            tags: empty_tags ? '' : this.shop.tags.map((tag) => tag['text']),
                            lat: this.shop.lat,
                            lng: this.shop.lng
                        },
                        {
                            arrayFormat :'repeat'
                        }
                    )
                ).then(() => {
                    this.err.suc=true;
                    this.err.error=false;
                    this.doReset();
                }).catch(err=>{alert(err);
                         this.err.error=true;
                         this.err.suc=false;})
            }
        });
  },
      markerChanged : function (data) {
          this.shop.lat = data[0];
          this.shop.lng = data[1];
          this.shop.address = data[2];
      },
    doReset: function(){
      this.$validator.reset();
      this.shop.name = '';
      this.shop.address = '';
      this.shop.tag = '';
      this.shop.tags = [];
    },
  },
}
</script>

<style scoped>
#add-shop *{
    box-sizing: border-box;
}
#add-shop{
    margin: 20px auto;
    max-width: 750px;
    max-height: 1000px;
}
label{
    display: block;
    margin: 20px 0 10px;
}
input[type="text"]{
    display: block;
    width: 100%;
    padding: 8px;
}

h3{
    margin-top: 10px;
}
.spacer {
    padding-top: 80px;
    padding-bottom: 40px;
}
</style>
