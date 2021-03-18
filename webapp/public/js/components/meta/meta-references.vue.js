export const template = `<table class="table table-sm table-borderless table-hover">
  <tr v-for="db in databases_filled">
    <th class="p-2"><img class="meta-db-icon" :src="'/img/dbicons/'+db+'.png'"> {{ db }}</th>
    <td>
      <div v-for="db_id in meta[db.lower()+'_id']">
        <a class="btn-block text-brand text-left p-1" :href="to_db_url(db_id, db.lower()+'_id')" :target="target">
          <b>{{ pad_id(db_id, db.lower()+'_id') }}</b>
        </a>
      </div>
    </td>
  </tr>
</table>`;