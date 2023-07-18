$("#get_cupcakes").click(getCupcakes);

let cupcakesArray = [];
let flavorsOnPage = [];

async function getCupcakes() {
  const response = await axios.get(`api/cupcakes`);
  const cupcakes = response.data.cupcakes;

  for (let cupcake of cupcakes) {
    if (!flavorsOnPage.includes(cupcake.flavor)) {
      $("#cupcakes_list").append(
        `<li class="text-capitalize">${cupcake.flavor}</li>`
      );
      flavorsOnPage.push(cupcake.flavor);
    }
  }
}

$("form").on("submit", async function (e) {
  e.preventDefault();

  const data = {
    flavor: $("#flavor").val().toLowerCase(),
    size: $("#size").val().toLowerCase(),
    rating: $("#rating").val(),
    image: $("#image").val(),
  };

  const response = await axios.post("api/cupcakes", data);
  console.log(response.data);

  $("form").trigger("reset");
});
