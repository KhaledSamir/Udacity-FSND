
(function () {

	var model = {
		currentCat: null,
		cats: [
			{
				clickCount: 0,
				name: 'Tabby',
				imgSrc: 'img/434164568_fea0ad4013_z.jpg',
				imgAttribution: 'https://www.flickr.com/photos/bigtallguy/434164568'
			},
			{
				clickCount: 0,
				name: 'Tiger',
				imgSrc: 'img/4154543904_6e2428c421_z.jpg',
				imgAttribution: 'https://www.flickr.com/photos/xshamx/4154543904'
			},
			{
				clickCount: 0,
				name: 'Scaredy',
				imgSrc: 'img/22252709_010df3379e_z.jpg',
				imgAttribution: 'https://www.flickr.com/photos/kpjas/22252709'
			},
			{
				clickCount: 0,
				name: 'Shadow',
				imgSrc: 'img/1413379559_412a540d29_z.jpg',
				imgAttribution: 'https://www.flickr.com/photos/malfet/1413379559'
			},
			{
				clickCount: 0,
				name: 'Sleepy',
				imgSrc: 'img/9648464288_2516b35537_z.jpg',
				imgAttribution: 'https://www.flickr.com/photos/onesharp/9648464288'
			}
		]
	}

	var Octupus = {
		init: function () {
			model.currentCat = model.cats[0];
			view.init();
			this.assignButtons();
		},
		getCats: function () {
			return model.cats;
		},
		setCurrentCat: function (num) {
			model.currentCat = model.cats[num];
		},
		getCurrentCat: function () {
			return model.currentCat;
		},
		increateCounter: function () {
			model.currentCat.clickCount++;
			view.render();
		},
		assignButtons: function () {
			var cats = this.getCats();
			for (var i = 0; i < cats.length; i++) {
				var button = $('#button' + (i + 1));
				$(button).click(function (num) {
					return function () {
						Octupus.setCurrentCat(num)
						view.render()
					}
				}(i))
			}
		}
	}

	var view = {

		init: function () {
			var catlistDiv = $('#catList');
			this.catName = document.getElementById('name');
			this.catCounter = document.getElementById('counter');
			this.catImg = document.getElementById('cat-img')

			var cats = Octupus.getCats();
			for (var i = 0; i < cats.length; i++) {
				var button = "<button id=" + "button" + (i + 1) + ">" + cats[i].name + "</button>";
				catlistDiv.append(button)
			}

			$(this.catImg).click(function () {
				Octupus.increateCounter();
			})

			this.render();
		},



		render: function () {
			var currentCat = Octupus.getCurrentCat();
			this.catName.textContent = currentCat.name;
			this.catCounter.innerText = currentCat.clickCount;
			this.catImg.src = currentCat.imgSrc;
		}
	}

	Octupus.init();
}());


