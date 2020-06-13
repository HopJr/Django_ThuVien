from django.db import models

# Create your models here.

sexChoice = ((1,'Nam'), (2, 'Nữ'), (3,'Khác...'))
class TacGia(models.Model):
    ma_TacGia =models.AutoField(primary_key = 'true', null = False)
    ten_Tacgia = models.CharField(max_length = 50)
    ghiChu = models.CharField(max_length = 255, null = 'true')
    def __str__(self):
        return self.ten_Tacgia
    class Meta:
        db_table ="TACGIA"
        managed = True
        verbose_name = 'Tác Giả'
        verbose_name_plural = 'Tác Giả'

class NhaXuatBan(models.Model):
    ma_NhaXuatBan = models.AutoField(primary_key ='true', null = False)
    ten_NhaXuatBan = models.CharField(max_length = 50)
    def __str__(self):
        return self.ten_NhaXuatBan
    
    class Meta:
        db_table = 'NHAXUATBAN'
        managed = True
        verbose_name = 'Nhà Xuất Bản'
        verbose_name_plural = 'Nhà Xuất Bản'

class TheLoai(models.Model):
    ma_TheLoai = models.AutoField(primary_key = 'true')
    ten_theLoai = models.CharField(max_length = 50)
    def __str__(self):
        return self.ten_theLoai
    class Meta:
        db_table = "THELOAI"
        managed = True
        verbose_name = 'Thể Loại'
        verbose_name_plural = 'Thể Loại'

class Sach(models.Model):
    ma_Sach = models.AutoField(primary_key ='true')
    ten_Sach =models.CharField(max_length = 50, null = False)
    tacGia = models.ForeignKey(TacGia, on_delete= models.CASCADE )
    loaiSach = models.ForeignKey(TheLoai , on_delete= models.CASCADE)
    nhaXuatBan = models.ForeignKey(NhaXuatBan, on_delete= models.CASCADE)
    soLuong = models.IntegerField(null= False)
    namXuatBan = models.IntegerField(null= False, default=2020)
    anh = models.ImageField(max_length= 255)
    def __str__(self):
        return  self.ten_Sach
    class Meta:
        db_table = "BOOK"
        managed = True
        verbose_name = 'Sách'
        verbose_name_plural = 'Sách'
class TopSach(models.Model):
    ma_TopSach = models.AutoField(primary_key = 'true')
    sach = models.ForeignKey(Sach, on_delete=models.CASCADE)    
    class Meta:
        db_table = 'TopSach'
        managed = True
        verbose_name = 'Top Sách'
        verbose_name_plural = 'Top Sách'
class NhaCungCap(models.Model):
    ma_nhaCungCap = models.AutoField(primary_key = 'true')
    ten_nhaCungCap  = models.CharField(max_length = 50)
    def __str__(self):
        return self.ten_nhaCungCap
    class  Meta:
        db_table = 'NHACUNGCAP'
        managed = True
        verbose_name = 'Nhà Cung Cấp'
        verbose_name_plural = 'Nhà Cung Cấp'

class NhanVien(models.Model):
    ma_NhanVien = models.AutoField(primary_key = 'true')
    HoTen = models.CharField(max_length =  50, null = False)
    DiaChi = models.CharField(max_length = 50 , null = False)
    SoDT = models.CharField (max_length = 11, null =False)
    CMND = models.CharField (max_length = 11, null = False)
    GioiTinh = models.IntegerField (choices= sexChoice)
    ma_nhaCungCap = models.ForeignKey(NhaCungCap, on_delete=models.CASCADE)
    def __str__(self):
        return self.HoTen
    class  Meta:
        db_table = 'NHANVIEN'
        managed = True
        verbose_name = 'Nhân Viên'
        verbose_name_plural = 'Nhân Viên'

class SinhVien(models.Model):
    ma_SinhVien = models.CharField(max_length = 50, primary_key = 'true', null =False)
    ten_SinhVien = models.CharField(max_length = 50, null = False)
    gioiTinh =models.IntegerField( null = False, choices = sexChoice)
    lop = models.CharField(max_length = 10, null = False)
    NamSinh = models.DateField()
    diaChi = models.CharField(max_length = 100, null = False)
    khoa = models.CharField(max_length = 20, null= False)
    username = models.CharField(max_length =20, null = False)
    password = models.CharField (max_length = 20, null = False)
    nhanVien = models.ForeignKey(NhanVien, on_delete= models.CASCADE)
    def __str__(self):
        return  self.ten_SinhVien
    class Meta:
        db_table = "sinhvien"
        managed = True
        verbose_name = 'Sinh Viên'
        verbose_name_plural = 'Sinh Viên'

class BaoCao(models.Model):
    ma_BaoCao = models.AutoField(primary_key = 'true')
    ngay = models.DateTimeField()
    ma_nhanVien = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    class Meta:
        db_table = 'BAOCAO'
        managed = True
        verbose_name = 'Báo Cáo'
        verbose_name_plural = 'Báo Cáo'

class PhieuYeuCau(models.Model):
    ma_PhieuYeuCau = models.AutoField(primary_key = 'true')
    ten_phieuYeuCau = models.CharField(max_length = 50, null = False)
    TenSach = models.ForeignKey(Sach, on_delete= models.CASCADE)
    soLuong = models.IntegerField(null= False)
    nhanVien = models.ForeignKey(NhanVien, on_delete= models.CASCADE)
    def __str__(self):
        return self.ten_phieuYeuCau

    class Meta:
        db_table = 'PHIEUYEUCAU'
        managed = True
        verbose_name = 'Phiếu Yêu Cầu'
        verbose_name_plural = 'Phiếu Yêu Cầu'
