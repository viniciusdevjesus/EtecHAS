namespace FaceCoin
{
    
    public partial class MainPage : ContentPage
    {
        int select = 0;

        public MainPage()
        {
            InitializeComponent();
        }

        private void ButtonChoice_Clicked(object sender, EventArgs e)
        {
            string ladoSelecionado = PickerChoice.SelectedItem.ToString();
            if (ladoSelecionado == "coroa")
                select = 1;
            else
                select = 0;

            
            int sort = new Random().Next(2);

            if (sort == 0)
                imgCoin.Source = "coroa.png";
            if (sort == 1) 
                imgCoin.Source = "cara.png";

            if (sort == select)
                DisplayAlert("Congratulations", "You Win", "Ok.");
            else
                DisplayAlert("Quak Quak", "You Lose", "Ok.");
        }
    }

}
