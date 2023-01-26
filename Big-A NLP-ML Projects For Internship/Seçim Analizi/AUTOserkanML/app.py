import os
import streamlit as st 

# EDA Pkgs
import pandas as pd 

# Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 

def main():
	""" Dataset Keşfi """
	st.title("ML Dataset Keşfedici")

	html_temp = """
	<div style="background-color:tomato;"><p style="color:white;font-size:50px;padding:10px"></p></div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)

	def file_selector(folder_path='C:/Users/SERKAN/Desktop/Big-A NLP/Seçim Analizi/AUTOserkanML'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Dosya Seçiniz",filenames)
		return os.path.join(folder_path,selected_filename)

	filename = file_selector()
	st.info("Seçiminiz {}".format(filename))

	# Read Data
	df = pd.read_csv(filename)
	# Show Dataset

	if st.checkbox("Veri Setini Göster"):
		number = st.number_input("Görüntülenecek Satır Sayısı")
		st.dataframe(df.head(number))

	# Show Columns
	if st.button("Sütun Adları"):
		st.write(df.columns)

	# Show Shape
	if st.checkbox("Veri Kümesinin Şekli"):
		data_dim = st.radio("Boyutu Göster ",("Satırlar","Sütunlar"))
		if data_dim == 'Satırlar':
			st.text("Satır sayısı")
			st.write(df.shape[0])
		elif data_dim == 'Sütunlar':
			st.text("Sütun sayısı")
			st.write(df.shape[1])
		else:
			st.write(df.shape)

	# Select Columns
	if st.checkbox("Gösterilecek Sütunları Seçin"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Seçme",all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df)
	
	# Show Values
	if st.button("Değer Sayıları"):
		st.text("Hedefe/Sınıfa Göre Değer Sayımları")
		st.write(df.iloc[:,-1].value_counts())


	# Show Datatypes
	if st.button("Data Types"):
		st.write(df.dtypes)



	# Show Summary
	if st.checkbox("Özet"):
		st.write(df.describe().T)

	## Plot and Visualization

	st.subheader("Veri goruntuleme")
	# Correlation
	# Seaborn Plot
	if st.checkbox("Korelasyon Grafiği[Seaborn]"):
		st.write(sns.heatmap(df.corr(),annot=True))
		st.pyplot()

	
	# Pie Chart
	if st.checkbox("Pasta Grafiği"):
		all_columns_names = df.columns.tolist()
		if st.button("Pasta Grafiği Oluştur"):
			st.success("Bir Pasta Grafiği Oluşturma")
			st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
			st.pyplot()

	# Count Plot
	if st.checkbox("Değer Sayımları Grafiği"):
		st.text("Hedefe Göre Değer Sayımları")
		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox("GroupBy'ye Birincil Columm",all_columns_names)
		selected_columns_names = st.multiselect("Sütunları Seçin",all_columns_names)
		if st.button("Grafik"):
			st.text("Grafik Oluştur")
			if selected_columns_names:
				vc_plot = df.groupby(primary_col)[selected_columns_names].count()
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind="bar"))
			st.pyplot()


	# Customizable Plot

	st.subheader("Özelleştirilebilir Grafik")
	all_columns_names = df.columns.tolist()
	type_of_plot = st.selectbox("Grafik Türünü Seçin",["area","bar","line","hist","box","kde"])
	selected_columns_names = st.multiselect("Çizilecek Sütunları Seçin",all_columns_names)

	if st.button("Grafik Oluştur"):
		st.success("{} için Özelleştirilebilir {} Grafiği Oluşturuluyor".format(type_of_plot,selected_columns_names))

		# Plot By Streamlit
		if type_of_plot == 'area':
			cust_data = df[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = df[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = df[selected_columns_names]
			st.line_chart(cust_data)

		# Custom Plot 
		elif type_of_plot:
			cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()

	st.sidebar.header("Uygulama hakkında")
	st.sidebar.info("Makine Öğrenimi Veri Kümesini Keşfetmek İçin Uygulama")

	st.sidebar.header("Veri kümelerini al")
	st.sidebar.markdown("[ML Veri Kümesi Deposu]("")")

	st.sidebar.header("Hakkında")
	st.sidebar.info("serkan@softforware.tech")
	st.sidebar.text("Serkan POLAT")


if __name__ == '__main__':
	main()
