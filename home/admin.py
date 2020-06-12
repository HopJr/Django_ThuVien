from django.contrib import admin
from .models import Sach, BaoCao, NhaCungCap, NhaXuatBan, NhanVien, PhieuYeuCau ,SinhVien, TheLoai,  TacGia, PhieuYeuCau
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display =['ma_TacGia', 'ten_Tacgia', 'ghiChu']

 #SashAdmin   
class BookAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    sortable_by = 'id'
    # date_hierarchy = 'created_at'
    search_fields = ['ma_Sach', 'ten_Sach', 'tacGia', 'loaiSach', 'nhaXuatBan', 'soLuong','namXuatBan']    
    list_display =['ma_Sach', 'ten_Sach', 'tacGia', 'loaiSach', 'nhaXuatBan', 'soLuong','namXuatBan', 'anh']    
    # list_display_links = ('book_name')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['ma_TheLoai', 'ten_theLoai']

class NhaXuatBanAdmin(admin.ModelAdmin):
    search_fields = ['ma_Sach', 'ten_Sach']
    list_display = ['ma_NhaXuatBan', 'ten_NhaXuatBan']

class NhanVienAdmin(admin.ModelAdmin):
    search_fields = ['HoTen', 'SoDT']
    list_display = ['ma_NhanVien', 'HoTen', 'DiaChi', 'SoDT', 'CMND', 'GioiTinh', 'ma_nhaCungCap']

# class SinhVienAdmin(admin.ModelAdmin):
#     search_fields = ['ma_SinhVien', 'ten_Sach']
#     list_display = ['ma_NhaXuatBan', 'ten_NhaXuatBan']

admin.site.register(TheLoai, CategoryAdmin)
admin.site.register(Sach, BookAdmin)
admin.site.register(TacGia, AuthorAdmin)
admin.site.register(NhaXuatBan, NhaXuatBanAdmin)
admin.site.register(NhanVien, NhanVienAdmin)
admin.site.register(SinhVien)
admin.site.register(NhaCungCap)
admin.site.register(BaoCao)
admin.site.register(PhieuYeuCau)


#admin header and title 
admin.site.site_header = "QL THƯ VIỆN | ADMIN DASHBOARD"
admin.site.site_title = 'Home'
admin.site.index_title = ''


