export const template = `<table class="table table-sm table-borderless table-hover">
  <tr v-for="db in databases_filled">
    <th class="text-success"><img class="meta-db-icon" :src="'/img/dbicons/'+db+'.png'"> {{ db }}</th>
    <td>{{ meta[db.lower()+"_id"].join(", ") }}</td>
  </tr>
</table>`;